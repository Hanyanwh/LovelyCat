$(function(){
		$.getJSON("backstage/update.json").done(function(data){
			var food_residue = data["food_residue"];
			var water_residue = data["water_residue"];
		  	var food_total = data["food_total"];
			var today_data = data["today_data"];
			var week_data = data["week_data"];
			var month_data = data["month_data"];

			
			$("p#hidden").text(food_total);

			var msg = '<h2><img src="images/food.png" />食物余量：'+ food_residue + 'g</h2></p>';
				msg += '<h2><img src="images/water.png" />水余量：'+ water_residue + 'g</h2></p>';
				$('div#residue').html(msg);

			Morris.Line({
				element: 'graph1',
				data: today_data,
				xkey: 'time',
				ykeys: ['food', 'water'],
				labels: ['food', 'water'],
				parseTime: false
			  });

			  Morris.Bar({
				element: 'graph5',
				data: week_data,
				xkey: 'x',
				ykeys: ['food', 'water'],
				labels: ['FOOD', 'WATER'],
				stacked: true
			  });

			  Morris.Bar({
				element: 'graph8',
				data: month_data,
				xkey: 'period',
				ykeys: ['food', 'water'],
				labels: ['FOOD', 'WATER'],
				xLabelAngle: 60 
				});

				$.getJSON("backstage/user_information.json").done(function(data){
					var kcal =  data["kcal"]*food_total/100;
					var protein = data["protein"]*food_total/100;
					var carbohydrate= data["carbohydrate"]*food_total/100;
					var fat = data["fat"]*food_total/100;
			
					var kcal_total = 10000;			// 成猫的每日卡路里
					var kcal_need = kcal_total - kcal;
					var maoliang_need = (kcal_need / data["kcal"]*100).toFixed(2);
					var nutrition = protein + carbohydrate + fat;
					var protein_rate = (protein/nutrition*100).toFixed(2);
					var carbohydrate_rate = (carbohydrate/nutrition*100).toFixed(2);
					var fat_rate = (fat/nutrition*100).toFixed(2);
			
					$("em#kcal_current").text(kcal);
					$("em#kcal_need").text(kcal_need);
					$("em#maoliang_need").text(maoliang_need);
			
					Morris.Donut({
						element: 'graph4',
						data: [
							{value: protein, label: 'protein', formatted: '蛋白质 '+ protein +'g' },
							{value: carbohydrate, label: 'carbohydrate', formatted: '碳水化合物'+ carbohydrate +'g' },
							{value: fat, label: 'fat', formatted: '脂肪'+  fat +'g' },
						],
						formatter: function (x, data) { return data.formatted; }
					});
				});
			});
			
});


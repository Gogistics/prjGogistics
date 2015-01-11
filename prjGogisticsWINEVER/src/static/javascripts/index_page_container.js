/**/

'use strict';
var index_page_app;

(function(){
	//
	var injected_module = [];
	injected_module = ['angular-responsive', 'ui.router', 'ngAnimate'];
	
	index_page_app = index_page_app || angular.module('indexPageApp', injected_module, function($interpolateProvider){
		$interpolateProvider.startSymbol('[[');
		$interpolateProvider.endSymbol(']]');
	});
	
	// set global values
	index_page_app.value('GLOBAL_VALUES', {
		EMAIL : 'gogistics@gogistics-tw.com',
		WINE_SEARCHER_API_KEY : 'http://api.wine-searcher.com/wine-select-api.lml?Xkey=ggstcs871585&Xversion=5'
	});
	
	// set config.
	index_page_app.config(function(responsiveHelperProvider, $stateProvider, $urlRouterProvider){
		
		// check which device user is using
		var device = 'desktop';
		var responsiveHelper = responsiveHelperProvider.$get();
		if(responsiveHelper.isMobile()){
			device = 'mobile';
		}else if(responsiveHelper.isTablet()){
			device = 'tablet';
		}
		
		// nested templates routing
		$stateProvider.state('home', {
			templateUrl : '/my_ng_templates/my_ng_template_base.html',
		}).state('index_page', {
			parent : 'home',
			templateUrl : '/my_ng_templates/' + device + '/index/index_page.html',
			controller : 'indexPageDispatchCtrl'
		}).state('index_wine_searcher', {
			url : '/index_wine_searcher',
			parent : 'index_page',
			templateUrl : '/my_ng_templates/' + device + '/index/index_wine_searcher.html'
		}).state('index_shipping_service', {
			url : '/index_shipping_service',
			parent : 'index_page',
			templateUrl : '/my_ng_templates/' + device + '/index/index_shipping_service.html'
		});
	});
	
	// dispatcher
	var indexPageDispatchController = function($state, $scope, GLOBAL_VALUES){
		$scope.email = GLOBAL_VALUES.EMAIL;
		
		//init page
		var selected_template = $state.current.name;
		if($state.current.name !== ''){
			$state.transitionTo(selected_template);
		} else{
			$state.transitionTo('index_wine_searcher');
		}
	}
	indexPageDispatchController.$inject = ['$state', '$scope', 'GLOBAL_VALUES'];
	index_page_app.controller('indexPageDispatchCtrl', indexPageDispatchController);
	// end of indexPageDispatchController
	
	// controller
	var indexPageController = function($state, $scope, GLOBAL_VALUES){
		//
		var current_ctrl = this, $list_block = $( "#list_block" ), $list_detail = $("#list_detail");
		current_ctrl.is_list_open = false, current_ctrl.selected = $state.current.name;
		
		// toggle list by list icon
		current_ctrl.toggle_list = function(){
			current_ctrl.is_list_open = !current_ctrl.is_list_open;
			
			if($list_block.hasClass( "fadeOutLeft")){
				$list_block.removeClass('fadeOutLeft');
				$list_detail.removeClass('list_display_none');
				$list_block.addClass('list_block_show fadeInLeft');
			}else{
				$list_block.removeClass('fadeInLeft');
				$list_block.addClass(' fadeOutLeft');
				$list_block.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){ 
					$list_block.removeClass('list_block_show');
					$list_detail.addClass('list_display_none');
				});
			}
		};
		
		// switch class
		current_ctrl.is_selected = function(arg_topic){
			return (current_ctrl.selected === arg_topic);
		}
		
		// select topic
		current_ctrl.select_topic = function(arg_topic){
			current_ctrl.selected = arg_topic;
			
			// switch topic
			current_ctrl.is_list_open = !current_ctrl.is_list_open;
			
			if($list_block.hasClass( "fadeOutLeft")){
				$list_block.removeClass('fadeOutLeft');
				$list_detail.removeClass('list_display_none');
				$list_block.addClass('list_block_show fadeInLeft');
			}else{
				$list_block.removeClass('fadeInLeft');
				$list_block.addClass(' fadeOutLeft');
				$list_block.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){ 
					$list_block.removeClass('list_block_show');
					$list_detail.addClass('list_display_none');
					
					// switch topic content
					$state.transitionTo(arg_topic);
				});
			}
		};
	};
	indexPageController.$inject = ['$state', '$scope', 'GLOBAL_VALUES'];
	index_page_app.controller('indexPageCtrl', indexPageController);
	// end
	
	
	// controller of querying wine info
	var wineInfoQueryController = function($http, $scope, GLOBAL_VALUES){
		// var
		var ctrl_this = this;
		$scope.wine = {"info" : undefined, "vintage" : undefined}; // default search info
		// vintage list
		ctrl_this.vintage = [];
		var current_year = new Date().getFullYear();
		for (var ith = 1600 ; ith <= current_year; ith++){
			ctrl_this.vintage.push(ith);
		}
		
		// get query vintage
		var get_query_vintage = function(arg_vintage){
			$scope.wine.vintage = arg_vintage; // set vintage
			
			console.log($scope.wine.vintage + " ; " + $scope.wine.info);
		}
		ctrl_this.get_query_vintage = get_query_vintage;
		
		// get query wine info
		var search_wine_info = function(){
			console.log($scope.wine.vintage + " ; " + $scope.wine.info);
			
			//
			if ($scope.wine.info !== undefined){
				$scope.wine.info = $scope.wine.info.trim();
				if ($scope.wine.info.length <= 0){
					alert("query string is empty!");
					return false;
				}
			}else{
				alert("query string is empty!");
				return false;
			}
			// query string for average price
			// var query_str = GLOBAL_VALUES.WINE_SEARCHER_API_KEY + "&Xformat=J" + "&Xwinename=" + "stag+leap+napa+usa" + "&Xvintage=" + "1999" + "&Xlocation=" + "&Xautoexpand=Y" + "&Xcurrencycode=usd" + "&Xkeyword_mode=X" + "&Xwidesearch=V";
			var query_data = $.param({ query_info : $scope.wine.info, query_vintage : $scope.wine.vintage });
			var req = {
					 method: 'POST',
					 url: '/query/wine_searcher',
					 headers: {
					   'Content-Type': 'application/x-www-form-urlencoded',
					 },
					 data: query_data,
				};

			// post query to server
			$http(req)
			.success(function(data, status, headers, config){
				var json_response = JSON.parse(data.query_results);
				var return_code = json_response['wine-searcher']['return-code'];
				console.log(json_response['wine-searcher']);
				
				ctrl_this.info_list = [];
				if(return_code === "0"){
					var currency = json_response['wine-searcher']['list-currency-code'];
					
					if(json_response['wine-searcher']['names'] !== undefined){
						for(var ith = 0 ; ith < json_response['wine-searcher']['names'].length; ith++){
							var wine_info = json_response['wine-searcher']['names'][ith]['name'];
							ctrl_this.info_list.push("Wine Name: " + wine_info['wine-name']);
							ctrl_this.info_list.push("Region: " + wine_info['region']);
							ctrl_this.info_list.push("Grape: " + wine_info['grape']);
							ctrl_this.info_list.push("Currency: " + currency);
							ctrl_this.info_list.push("Avg. Price: " + wine_info['price-average']);
							ctrl_this.info_list.push("Min. Price: " + wine_info['price-min']);
							ctrl_this.info_list.push("Max. Price: " + wine_info['price-max']);
						}
					}
					else if(json_response['wine-searcher']['wine-vintages'] !== undefined){
						for(var ith = 0 ; ith < json_response['wine-searcher']['wine-vintages'].length; ith++){
							var wine_info = json_response['wine-searcher']['wine-vintages'][ith]['wine-vintage'];
							if(wine_info['vintage'].length < 3){
								continue;
							}
							var str = "Wine: " + $scope.wine.info + " ; " +
									  "Vintage: " + wine_info['vintage'] + " ; " + 
									  "Currency: " + currency + " ; " +
									  "Avg. Price: " + wine_info['price-average'] + " ; " +
									  "Max. Price: " + wine_info['price-max'] + " ; " +
									  "Min. Price: " + wine_info['price-min'];
							console.log(str);
							ctrl_this.info_list.push(str);
						}
					}
				}else{
					ctrl_this.info_list.push("No Related Information");
				}
			})
			.error(function(data, status, headers, config){
				console.log(status);
			});
			// end of query
			
			
			// something wrong with get json query response from Wine Searcher; the error can be solved by passing query back to server
			/*$.getJSON( query_str + "&callback=?", function(data, textStatus, jqXHR){
				   //response data are now in the result variable
				   alert(data);
				})
				.success(function(data, textStatus, jqXHR) { alert("second success"); })
				.error(function(data, textStatus, jqXHR) { alert(JSON.stringify(data,2,2)); })
				.complete(function(data, textStatus, jqXHR) { alert(JSON.stringify(data,2,2)); });
			*/
			/*$.ajax(query_str, {
			    crossDomain:true, 
			    dataType: "jsonp", 
		        async: false,
			    success:function(data,text,xhqr){
			        $.each(data, function(i, item) {
			            alert(item);
			        });
			    }
			});*/
		}
		ctrl_this.search_wine_info = search_wine_info;
	};
	wineInfoQueryController.$inject =['$http', '$scope', 'GLOBAL_VALUES'];
	index_page_app.controller('wineInfoQueryCtrl', wineInfoQueryController);
	// end
	
	var vintageFilter = function(){
		return function(input, total){
			var current_year = new Date().getFullYear();
			// total = parseInt(total); // total can be assigned from view
			for(var i = 0; i <= current_year; i++){
				input.push(i);
			}

			return input;
		};
	};
	index_page_app.filter('range', vintageFilter);
	// end
	
})();
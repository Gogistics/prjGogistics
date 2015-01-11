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
		var current_ctrl = this, $list_block = $( "#list_block" ), $list_detail = $("#list_detail");
		current_ctrl.is_list_open = false;
		
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
		}
	};
	indexPageController.$inject = ['$state', '$scope', 'GLOBAL_VALUES'];
	index_page_app.controller('indexPageCtrl', indexPageController);
	// end
	
	
	// controller of querying wine info
	var wineInfoQueryController = function($scope, GLOBAL_VALUES){
		// var
		var ctrl_this = this;
		$scope.wine = {"info" : undefined, "vintage" : undefined}; // default search info
		
		var wine_vintage, wine_info; // query var
		// get query vintage
		var get_query_vintage = function(arg_vintage){
			console.log(arg_vintage + " ; " + $scope.wine.info);
		}
		ctrl_this.get_query_vintage = get_query_vintage;
		
		// get query wine info
		var search_wine_info = function(){
			
			// query string for average price
			var query_str = GLOBAL_VALUES.WINE_SEARCHER_API_KEY + "&Xformat=J" + "&Xwinename=" + "stag+leap+napa+usa" + "&Xvintage=" + "1999" + "&Xlocation=" + "&Xautoexpand=Y" + "&Xcurrencycode=usd" + "&Xkeyword_mode=X" + "&Xwidesearch=V";
			

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
			
			console.log($scope.wine.vintage + " ; " + $scope.wine.info);
		}
		ctrl_this.search_wine_info = search_wine_info;
		
	};
	wineInfoQueryController.$inject =['$scope', 'GLOBAL_VALUES'];
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
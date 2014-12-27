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
		}).state('index_introduction', {
			url : '/index_introduction',
			parent : 'index_page',
			templateUrl : '/my_ng_templates/' + device + '/index/index_introduction.html'
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
			$state.transitionTo('index_introduction');
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
	}
	indexPageController.$inject = ['$state', '$scope', 'GLOBAL_VALUES'];
	index_page_app.controller('indexPageCtrl', indexPageController);
	// end
	
})();
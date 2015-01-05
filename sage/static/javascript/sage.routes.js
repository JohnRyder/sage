(function(){
	'use strict';
    
    angular
    	.module('sage.routes')
    	.config(config);
    
    config.$inject = ['$routeProvider'];
    
    function config($routeProvider){
        $routeProvider.when('/register', {
            controller: 'RegisterController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/accounts/register.html'
        }).otherwise('/');
    }

}());
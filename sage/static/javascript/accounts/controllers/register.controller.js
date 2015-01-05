(function(){
    'use strict';

	angular
    	.module('sage.accounts.controllers')
    	.factory('RegisterController', RegisterController);
    
    RegisterController.$inject = ['$location', '$scope', 'Accounts'];
    
    function RegisterController($location, $scope, Accounts){
        var vm = this;
        
        vm.register = register;
        
        function register(){
            Accounts.register(vm.email, vm.password, vm.username);
        }
    }
    
}());
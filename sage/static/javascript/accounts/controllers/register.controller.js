(function(){
    'use strict';

	angular
    	.module('sage.accounts.controllers')
    	.controller('RegisterController', RegisterController);
    
    RegisterController.$inject = ['$scope', 'Accounts'];
    
    function RegisterController($scope, Accounts){
        var vm = this;
        
        vm.register = register;
        
        function register(){
            Accounts.register(vm.email, vm.password, vm.username);
        }
    }
    
})();
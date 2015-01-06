(function(){
	'use strict';
    
    angular
    	.module('sage', [
        	'sage.routes',
        	'sage.accounts'
        ])
    	.run(run);
    
    angular
    	.module('sage.routes', ['ngRoute']);
    
    run.$inject = ['$http'];

    function run($http) {
    	$http.defaults.xsrfHeaderName = 'X-CSRFToken';
    	$http.defaults.xsrfCookieName = 'csrftoken';
    } 

})();
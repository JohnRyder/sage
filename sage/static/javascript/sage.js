(function(){
	'use strict';
    
    angular
    	.module('sage', [
        	'sage.routes',
        	'sage.accounts'
        ]);
    
    angular
    	.moudule('sage.routes', [$ngRoute]);

}());
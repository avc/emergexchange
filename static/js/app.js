var indexApp = angular.module('indexApp', []);

var accountApp = angular.module('accountApp', []);

var exchangeApp = angular.module('exchangeApp', []);

var app = angular.module('app', ['indexApp', 'accountApp', 'exchangeApp']);

app.run(
    ['$rootScope', '$window',
        function ($rootScope, $window) {

            var currentUser = JSON.parse(localStorage.getItem('currentUser'));
            if(!currentUser) {
            	$rootScope.authenticated = false;
            } else {
            	$rootScope.currentUserId = currentUser.id;
            	$rootScope.authenticated = true;
            }
            if(!$rootScope.authenticated && !$window.location.href.match('index.html')) {
            	$window.location.href = 'index.html';
            	console.log("match");
            } else {
            	console.log('Didnt Match');
            }

        }
    ]
);
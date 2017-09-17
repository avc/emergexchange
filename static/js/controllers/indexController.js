app.controller('indexController', ['$scope', '$rootScope', '$window', '$http', function($scope, $rootScope, $window, $http) {

	$scope.user_login = {
		'username': '',
		'password': ''
	}

	$scope.signup = {
		'username': '',
		'password': '',
		'conf_password': '',
		'email': ''
	}

	$scope.login = function() {
		console.log($scope.user_login);
		$http.post("http://emergexchange.com/accounts/login/", $scope.user_login).then(function(response){
            console.log("Hey");
            console.log(response);
        });
	}

	$scope.signup = function() {
		if($scope.signup.password === $scope.signup.conf_password){
			$http.post("http://emergexchange.com/accounts/create-user/", {
				'username': $scope.signup.username,
				'password': $scope.signup.password,
				'email': $scope.signup.email
			},
			{
                headers: {
                }
            }).then(function(response){
            	console.log("Hey");
            	console.log(response);
            });
		}
	}	

}]);
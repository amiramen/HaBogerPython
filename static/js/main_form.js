/**
 * Created by amiram on 10/17/2016.
 */

var app = angular.module('myApp', []);
        app.controller('myCtrl', function($scope, $http) {
            $http.get("/get_form_data")
            .then(function(response) {
                console.log(response.data);
                window.myWelcome = response.data;
            });
        });
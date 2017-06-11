/**
 * Created by amiram on 10/17/2016.
 */

var app = angular.module('myApp', []);
        app.controller('myCtrl', function($scope, $http) {
            $http.get("/get_form_data")
            .then(function(response){build_form(response,$scope)});

        });

function build_form(server_response, $scope){

    nodes = server_response.data;
    $scope.myWelcome = "hey!!"
    // TODO: add the specific <DIV> tag name to be correct by angularJS
    //add_node("node name by angular HERE...", nodes)
}

function add_node(father_node, json_node){
    angular.forEach(json_node, function(value,key){
        console.log(value);
        console.log(key);
    });
}
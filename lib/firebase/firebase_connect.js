const firebase = require("firebase");


var firebaseConfig = {
    apiKey: "AIzaSyDeRB3tq2VZGtwAOyUh9xIrX9x5BIF6w14",
    authDomain: "whatowatch-1eb80.firebaseapp.com",
    // The value of `databaseURL` depends on the location of the database
    databaseURL: "https://whatowatch-1eb80-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "whatowatch-1eb80",
    storageBucket: "whatowatch-1eb80.appspot.com",
    messagingSenderId: "969308943808",
    appId: "APP_ID"
  };
  
  firebase.initializeApp(firebaseConfig);
  
  // Get a reference to the database service
  var database = firebase.database();

const app = firebase()
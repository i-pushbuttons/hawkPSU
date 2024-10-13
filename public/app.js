import { initializeApp } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-app.js";
import { getAuth, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-firestore.js";
import { getDatabase } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-database.js";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyD6RAw-E2MBugeP4RqJYCQnzDFf5jJSu-8",
    authDomain: "competitive-stem.firebaseapp.com",
    projectId: "competitive-stem",
    storageBucket: "competitive-stem.appspot.com",
    messagingSenderId: "530749112009",
    appId: "1:530749112009:web:5944d962cef9aef95c9718",
    measurementId: "G-C8E0PPJG62"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const database = getDatabase(app);

// Example usage of Firebase Auth
onAuthStateChanged(auth, (user) => {
    if (user) {
        console.log('User is signed in:', user);
    } else {
        console.log('No user is signed in.');
    }
});

// Add any additional Firebase functionality here

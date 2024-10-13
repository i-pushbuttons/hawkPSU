// import {getFirestore, doc, setDoc, getDoc, updateDoc} from 'https://www.gstatic.com/firebasejs/10.14.1/firebase-firestore.js';

// const db = getFirestore();

// async function sendChallenge() {
//   const challengedUser = document.getElementById('challengeUser').value.trim();
//   const currentUser = 'currentUserId'; // Replace with actual current user ID

//   if (!challengedUser) {
//     alert('Please enter a username to challenge.');
//     return;
//   }

//   if (challengedUser === currentUser) {
//     alert('You cannot challenge yourself.');
//     return;
//   }

//   const challengedUserRef = doc(db, 'users', challengedUser);
//   const challengedUserDoc = await getDoc(challengedUserRef);

//   if (!challengedUserDoc.exists()) {
//     alert('The user you are trying to challenge does not exist.');
//     return;
//   }

//   const challengeRef = doc(db, 'challenges', `${currentUser}_${challengedUser}`);
//   await setDoc(challengeRef, {
//     challenger: currentUser,
//     challenged: challengedUser,
//     status: 'pending',
//   });

//   alert(`Challenge sent to ${challengedUser}`);
//   // Here you could add logic to notify the challenged user
// }

// async function acceptChallenge(challengeId) {
//   const challengeRef = doc(db, 'challenges', challengeId);
//   const challengeDoc = await getDoc(challengeRef);

//   if (challengeDoc.exists() && challengeDoc.data().status === 'pending') {
//     await updateDoc(challengeRef, {
//       status: 'accepted',
//     });

//     // Notify both users and redirect to GameOn.html
//     window.location.href = 'GameOn.html';
//   } else {
//     alert('Challenge not found or already accepted.');
//   }
// }

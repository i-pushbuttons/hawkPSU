function updateRanking(userId, score) {
    const userRef = firestore.collection('users').doc(userId);
    userRef.get().then((doc) => {
        if (doc.exists) {
            const currentScore = doc.data().score || 0;
            userRef.update({ score: currentScore + score });
        } else {
            userRef.set({ score: score });
        }
    });
}

function getLeaderboard() {
    return firestore.collection('users')
        .orderBy('score', 'desc')
        .limit(10)
        .get()
        .then((querySnapshot) => {
            const leaderboard = [];
            querySnapshot.forEach((doc) => {
                leaderboard.push(doc.data());
            });
            return leaderboard;
        });
}

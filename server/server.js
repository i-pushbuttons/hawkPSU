// server.js
require('dotenv').config();
const express = require('express');
const { MongoClient, ObjectId } = require('mongodb');
const path = require('path');

const app = express();
const port = 3000;
const uri = process.env.MONGO_URI; // Replace with your MongoDB connection string

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, '../public')));

app.get('/get-problem', async (req, res) => {
    const client = new MongoClient(uri);

    try {
        await client.connect();
        const database = client.db('Fall2024');
        const collection = database.collection('HackPSU.Integral');

        const query = { "_id": new ObjectId("670b9058065baeea7b36299b") };
        const document = await collection.findOne(query);

        if (document) {
            res.json({ problem: document.problem });
        } else {
            res.status(404).json({ error: 'No document found' });
        }
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Error connecting to the database' });
    } finally {
        await client.close();
    }
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});

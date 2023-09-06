const express = require('express');
const app = express();
const pgp = require('pg-promise')();
const db = pgp('postgresql://admin_1:admin_1@localhost:5432/Virtucare');

app.get('/api/Patients', async (req, res) => {
  try {
    const data = await db.any('SELECT * FROM Patients');
    res.json(Patients);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

const PORT = process.env.PORT || 3000; // Use the specified environment port or default to 3000

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

// Serve all assets inside the 'public' folder dynamically
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
    console.log(`🚀 YOLOv26 Server running smoothly at http://localhost:${PORT}`);
});
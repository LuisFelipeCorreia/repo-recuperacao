const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('Rota principal a funcionar perfeitamente no Docker!'));
app.listen(3000, () => console.log('Servidor a correr na porta 3000'));
const express = require('express');
const router = require('./routes/router');

const colors = {
	green: '\x1b[32m',
	cyan: '\x1b[36m',
	red: '\x1b[31m',
	reset: '\x1b[0m'
};

const PORT = 3001;

const app = express();

app.use(express.json());
app.use(router);

app.listen(PORT, async () => {
	console.info(
		`\nServer running on port ${colors.green}${PORT}${colors.reset}`,
		`\n➜  Local: ${colors.cyan}http://localhost:${PORT}/${colors.reset}`
	);
});
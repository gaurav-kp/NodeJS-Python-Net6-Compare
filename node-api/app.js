const express = require("express");

const app = express();
const port = 1111;
app.listen(port, () => {
  console.log("listen port 1111");
});

//create api
app.get("/get_random", (req, res) => {
  res.json({ randon_number: Math.random() });
});

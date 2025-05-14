const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// MongoDB connection URI
mongoose.connect('mongodb+srv://yakaveeraratnala2004:sujithep@cluster0.lq3uyy4.mongodb.net/profileDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Middleware to parse incoming JSON requests
app.use(bodyParser.json());

// Create a schema for the user data
const userSchema = new mongoose.Schema({
  full_name: String,
  email: String,
  password: String,
  confirm_password: String,
});

// Create a model based on the schema
const User = mongoose.model('User', userSchema);

// Serve HTML file for the landing page
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/fp1.html');
});

// Register route
app.route('/register')
  .get((req, res) => {
    res.sendFile(__dirname + '/register.html');
  })
  .post((req, res) => {
    const userData = req.body;

    // Create a new user using the User model
    const newUser = new User(userData);

    // Save the user to the database
    newUser.save()
      .then(() => {
        res.status(200).send('User data saved successfully');
      })
      .catch((err) => {
        console.error(err);
        res.status(500).send(`Internal Server Error: ${err.message}`);
      });
  });

// Login route
app.route('/login')
  .get((req, res) => {
    res.sendFile(__dirname + '/login.html');
  })
  .post(async (req, res) => {
    const { email, password } = req.body;

    // Check if the user exists in the database
    const user = await User.findOne({ email, password }).exec();

    if (user) {
      // Successful login, redirect to the homepage
      res.redirect('/homepage');
    } else {
      res.status(401).send('Invalid login credentials');
    }
  });

// Homepage route
app.get('/homepage', (req, res) => {
  // Render the homepage with a navigation bar
  res.sendFile(__dirname + '/homepage.html');
});

// Profile route
app.get('/profile', (req, res) => {
  // Retrieve the user details from the database and render the profile page
  // For simplicity, assuming the user is already authenticated (you might want to add authentication middleware)
  User.findOne({ /* Add criteria to find the user, e.g., using a user ID */ })
    .then(user => {
      // Render the profile page with user details
      res.sendFile(__dirname + '/profile.html');
    })
    .catch(err => {
      console.error(err);
      res.status(500).send('Internal Server Error');
    });
});

// Your existing routes...
app.get('/products', (req, res) => {
  res.sendFile(__dirname + '/products.html');
});

app.get('/supplier', (req, res) => {
  res.sendFile(__dirname + '/supplier.html');
});

app.get('/stockout', (req, res) => {
  res.sendFile(__dirname + '/stockout.html');
});

app.get('/obsolete', (req, res) => {
  res.sendFile(__dirname + '/obsolete.html');
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

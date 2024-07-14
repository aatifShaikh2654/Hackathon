import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from './dashboard/Dashboard';
import Register from './components/Register'
import Login from './components/Login';
import Navbar from './components/Navbar';

function App() {

  // const { getUser } = useContext(UserContext)
  // const token = localStorage.getItem("token")

  // useEffect(() => {
  //   if (token) {
  //     getUser();
  //   }
  // }, [token])


  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route path='/' element={<Dashboard />} />
          <Route path='/login' element={<Login />} />
          <Route path='/register' element={<Register />} />
        </Routes>
      </Router>
    </>
  );
}

// Test
export default App;

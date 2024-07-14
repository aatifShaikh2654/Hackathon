import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from './dashboard/Layout';
import Dashboard from './dashboard/Dashboard';
import Register from './components/Register'
import Login from './components/Login';

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
        <Routes>
          <Route path='/' element={<Register />} />
          <Route path='/login' element={<Login/>} />
          <Route exact path="/dashboard" element={<Layout />}>
            <Route index element={<Dashboard />} />
          </Route>
        </Routes>
      </Router>
    </>
  );
}

// Test
export default App;

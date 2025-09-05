import { useEffect, useState } from 'react';
import LoginPage from './pages/login';
import RegisterPage from './pages/register';
import DashboardPage from './pages/Dashboard';
import Transactions from './pages/transactions';

const api_url = 'http://127.0.0.1:8000/api'

const styles = {
container: {
maxWidth: '600px',
margin: '40px auto',
padding: '20px',
fontFamily: 'Arial, sans-serif',
backgroundColor: '#fff',
borderRadius: '10px',
boxShadow: '0 4px 10px rgba(0, 0, 0, 0.1)',
},
form: {
padding: '15px',
backgroundColor: '#f8f9fa',
borderRadius: '8px',
marginBottom: '20px',
},
list: {
listStyle: 'none',
padding: 0,
},
error: {
color: '#d32f2f',
backgroundColor: '#ffebee',
padding: '12px',
borderRadius: '6px',
marginBottom: '16px',
fontSize: '14px',
},
logoutBtn: {
backgroundColor: '#d32f2f',
color: 'white',
border: 'none',
padding: '8px 16px',
borderRadius: '6px',
cursor: 'pointer',
float: 'right',
fontSize: '14px',
},
};


function App() {
  const [user, setUser] = useState(null);

  const handleLogout = () => {
    localStorage.removeItem("access");
    setUser(null);
  };

  if (!user) {
    return (
      <div>
        <h1>SberPank</h1>
        <LoginPage onLogin={setUser} />
        <RegisterPage onRegister={setUser} />
      </div>
    );
  }

  return <DashboardPage user={user} onLogout={handleLogout} />;
}

export default App;

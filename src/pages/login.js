import { useState } from 'react';
import { loginUser } from '../services/api';

export default function LoginPage({ onLogin }) {
  const [error, setError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    try {
      const data = await loginUser({
        username: formData.get('username'),
        password: formData.get('password'),
      });
      localStorage.setItem('access', data.access);
      onLogin(data.user);
    } catch {
      setError("Ошибка входа");
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <h3>Вход</h3>
      {error && <p style={{color:"red"}}>{error}</p>}
      <input name="username" placeholder="Логин" required />
      <input name="password" type="password" placeholder="Пароль" required />
      <button type="submit">Войти</button>
    </form>
  );
}

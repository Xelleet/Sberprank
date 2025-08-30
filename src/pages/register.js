import { useState } from 'react';
import { registerUser } from '../services/api';

export default function RegisterPage({ onReg }) {
  const [error, setError] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    localStorage.removeItem('access');
    const formData = new FormData(e.target);
    try {
      const data = await registerUser({
        username: formData.get('username'),
        email: formData.get('email'),
        first_name: formData.get('first_name'),
        last_name: formData.get('last_name'),
        password: formData.get('password'),
        password_confirm: formData.get('password_confirm'),
      });
      localStorage.setItem('access', data.access);
      onReg(data.user)
    } catch {
      setError("Ошибка входа");
    }
  };

  return (
    <form onSubmit={handleRegister}>
      <h3>Регистрация</h3>
      {error && <p style={{color:"red"}}>{error}</p>}
      <input name="username" placeholder="Username" required />
      <input name="email" placeholder="Email" required />
      <input name="first_name" placeholder="First name" required />
      <input name="last_name" placeholder="Last name" required />
      <input name="password" type="password" placeholder="Пароль" required />
      <input name="password_confirm" placeholder="Password confirm" required />
      <button type="submit">Войти</button>
    </form>
  );
}

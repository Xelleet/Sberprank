import { useState } from 'react';
import { createAccount } from '../services/api'; 
import '../styles/create_account.css'

export default function CreateAccountForm({ onAccountCreated }) {
  const [formData, setFormData] = useState({
    currency: 'RUB'
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const data = await createAccount({
        currency: formData.currency
      });
      console.log(formData)
      onAccountCreated(data);
      setFormData({ currency: 'RUB' }); 
    } catch (err) {
      setError(err.response?.data?.message || "Ошибка при создании счета");
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  return (
    <div className="create-account-form">
      <h3>Создать новый счет</h3>
      
      {error && <p className="error-message">{error}</p>}
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="currency">Выберите валюту:</label>
          <select
            id="currency"
            name="currency"
            value={formData.currency}
            onChange={handleChange}
            required
            className="form-select"
          >
            <option value="USD">USD - Доллар США</option>
            <option value="EUR">EUR - Евро</option>
            <option value="RUB">RUB - Российский рубль</option>
          </select>
        </div>

        <button 
          type="submit" 
          className="submit-btn"
          disabled={loading}
        >
          {loading ? 'Создание...' : 'Создать счет'}
        </button>
      </form>
    </div>
  );
}
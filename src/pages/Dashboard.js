import { useState, useEffect } from 'react';
import { fetchAccounts, transferMoney } from '../services/api';
import Transactions from './transactions';
import LoanManager from './LoanManager';
import '../styles/dashboard.css';
import CreateAccount from './create_account';

export default function DashboardPage({ user, onLogout }) {
  const [accounts, setAccounts] = useState([]);
  const [transferData, setTransferData] = useState({
    from_account_id: "",
    to_account_id: "",
    amount: "",
    description: "",
  });
  const [error, setError] = useState("");

  useEffect(() => {
    fetchAccounts().then(setAccounts).catch(() => setError("Не удалось загрузить счета"));
  }, []);

  const handleTransferChange = (e) => {
    setTransferData({ ...transferData, [e.target.name]: e.target.value });
  };

  const handleTransfer = async (e) => {
    e.preventDefault();
    try {
      await transferMoney(transferData);
      alert("Перевод выполнен");
      setTransferData({ from_account_id: "", to_account_id: "", amount: "", description: "" });
      const data = await fetchAccounts();
      setAccounts(data);
    } catch {
      setError("Ошибка перевода");
    }
  };

  return (
  <div className="dashboard-container">
    <div className="dashboard-header">
      <h1>Добро пожаловать, {user?.username}</h1>
      <button className="logout-btn" onClick={onLogout}>Выйти</button>
    </div>
    
    {error && <p className="error-message">{error}</p>}
    
    <section className="accounts-section">
      <h2>Ваши счета</h2>
      <ul className="accounts-list">
        {accounts.map(acc => (
          <li className="account-item" key={acc.id}>
            {acc.account_number} ({acc.currency}) - {acc.balance}
          </li>
        ))}
      </ul>
    </section>

    <section className="transfer-section">
      <h2>Перевод средств</h2>
      <form className="transfer-form" onSubmit={handleTransfer}>
        <div className="form-group">
          <select name="from_account_id" value={transferData.from_account_id} onChange={handleTransferChange} required>
            <option value="">С какого счета</option>
            {accounts.map(acc => (
              <option key={acc.id} value={acc.id}>{acc.account_number} ({acc.balance})</option>
            ))}
          </select>
        </div>
        
        <div className="form-group">
          <input name="to_account_id" type="number" placeholder="ID получателя" value={transferData.to_account_id} onChange={handleTransferChange} required />
        </div>
        
        <div className="form-group">
          <input name="amount" type="number" step="0.01" placeholder="Сумма" value={transferData.amount} onChange={handleTransferChange} required />
        </div>
        
        <div className="form-group">
          <input name="description" placeholder="Описание" value={transferData.description} onChange={handleTransferChange} />
        </div>
        
        <button className="transfer-btn" type="submit">Перевести</button>
      </form>
    </section>

    <section className='create-account-section'>
      <CreateAccount/>
    </section>
    
    <section className="transactions-section">
      <Transactions/>
    </section>
    
    <section className="loan-manager-section">
      <LoanManager/>
    </section>
  </div>
);
}

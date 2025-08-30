import { useState, useEffect } from 'react';
import { fetchAccounts, transferMoney } from '../services/api';
import Transactions from './transactions';
import LoanManager from './LoanManager';

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
    <div>
      <h1>Добро пожаловать, {user?.username}</h1>
      <button onClick={onLogout}>Выйти</button>
      {error && <p style={{color:"red"}}>{error}</p>}
      <h2>Ваши счета</h2>
      <ul>
        {accounts.map(acc => (
          <li key={acc.id}>{acc.account_number} ({acc.currency}) - {acc.balance}</li>
        ))}
      </ul>

      <h2>Перевод средств</h2>
      <form onSubmit={handleTransfer}>
        <select name="from_account_id" value={transferData.from_account_id} onChange={handleTransferChange} required>
          <option value="">С какого счета</option>
          {accounts.map(acc => (
            <option key={acc.id} value={acc.id}>{acc.account_number} ({acc.balance})</option>
          ))}
        </select>
        <input name="to_account_id" type="number" placeholder="ID получателя" value={transferData.to_account_id} onChange={handleTransferChange} required />
        <input name="amount" type="number" step="0.01" placeholder="Сумма" value={transferData.amount} onChange={handleTransferChange} required />
        <input name="description" placeholder="Описание" value={transferData.description} onChange={handleTransferChange} />
        <button type="submit">Перевести</button>
      </form>
      <Transactions/>
      <LoanManager/>
    </div>
  );
}

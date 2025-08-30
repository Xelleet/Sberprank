import React, {useState, useEffect} from 'react';
import '../styles/transactions.css';

const Transactions = () => {
    const[transactions, setTransactions] = useState([]);
const[isLoading, setIsLoading] = useState(true);
const[error, setError] = useState('');
const[form, setForm] = useState({
    from_account_id: "",
    to_account_id: "",
    amount: "",
    description: ""
});

const fetchTransactions = async() => {
    try{
        const token = localStorage.getItem('access');
        const response = await fetch('http://127.0.0.1:8000//api/transactions/', {
            method: "GET",
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            }
        });
        if(!response.ok) throw new Error('Не удалось загрузить транзакции');
        const data = await response.json();
        console.log(data);
        setTransactions(data);
    }
    catch(err){
        setError(err.message);
    }
    finally{
        setIsLoading(false);
    }
}

useEffect(() => {
    fetchTransactions();
}, []);

const handleCHange = (e) => {
    const {name, value} = e.target;
    setForm({...form, [name]:value});
}
if (isLoading){
    return <div className='loading'>Загрузка транзакций...</div>
}
return(
<div>
    <div className='transactions-container'>
        <h2>История транзакций</h2>
        <ul className='transactions-list'>
            {transactions.length === 0 ? (
                <li className='no-transactions'>Нет транзакций</li>
            ) : (
                transactions.map((tx) => (
                    <li key={tx.id} className='transactions-item'>
                        <div>
                            <strong>Тип:</strong> {tx.transaction_type}
                        </div>
                        <div>
                            <strong>Отправитель:</strong> {tx.from_account?.id} ({tx.from_account?.currency})
                        </div>
                        <div>
                            <strong>Получатель:</strong> {tx.to_account?.id} ({tx.to_account?.currency0})
                        </div>
                        <div>
                            <strong>Отправлено:</strong> {tx.amount} {tx.from_account?.currency}
                        </div>
                        {tx.received_amount && (
                <div>
    <strong>Получено:</strong> {Number(tx.received_amount).toFixed(2)} {tx.to_account?.currency}
  </div>
              )}
              {tx.fee > 0 && (
                <div>
                  <strong>Комиссия:</strong> {tx.fee} {tx.from_account?.currency}
                </div>
              )}
              {tx.exchange_rate && (
                <div>
                  <strong>Курс:</strong> 1 {tx.from_account?.currency} = {tx.exchange_rate} {tx.to_account?.currency}
                </div>
              )}
              <div>
                <strong>Статус:</strong> <span className={`status ${tx.status}`}>{tx.status}</span>
              </div>
              <div>
                <strong>Дата:</strong> {new Date(tx.timestamp).toLocaleString()}
              </div>
              {tx.description && (
                <div>
                    <strong>Описание:</strong> {tx.description}
                </div>
              )}
                    </li>
                ))
            )}
        </ul>
    </div>
</div>
)
}

export default Transactions;
import React, {useEffect, useState} from "react";
import {API_URL} from '../services/api'
import axios from 'axios';
import '../styles/loans.css';

const LoanManager = () => {
    const[step, setStep] = useState('list');
    const[isLoading, setIsLoading] = useState(true);
    const[errors, setErrors] = useState('');
    const[loans, setLoans] = useState([]);
    const[selectedLoan, setSelectedLoan] = useState(null);

    const[formData, setFormData] = useState({
        account_id: "",
        amount: "",
        term_monts: "",
    });
    const[accounts, setAccounts] = useState([]);

    useEffect(() => {
        const fetchAccounts = async() => {
            try{
                const res = await axios.get(API_URL + '/accounts', {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('access')}`
                    }
                })
                setAccounts(res.data)
            }catch (err){
                console.error(err);
            }
        }
        fetchAccounts();
        fetchLoans();
    }, []);

    const fetchLoans = async() => {
        setIsLoading(true);
        try{
            const res = await axios.get(`${API_URL}/loans/`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('access')}`
                }
            })
            setLoans(res.data);
            setErrors("")
        }catch (err){
            console.log(err);
        }
        finally{
            setIsLoading(false);
        }
    }

    const handleSubmit = async(e) => {
        e.preventDefault();
        setErrors("");
        try{
            const res = await axios.post(`${API_URL}/loans/apply/`, formData, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('access')}`
                }
            })
            setLoans([res.data, ...loans]);
            setFormData({account_id: "", amount: "", term_monts: ""})
            setStep('list')
        }catch(err){
            console.log(err);
            setErrors("Ошибка при подаче заявки")
        }
    }

    const handleDetail = async(loanID) => {
        setIsLoading(true);
        try{
            const res = await axios.get(`${API_URL}/loans/${loanID}/`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('access')}`
                }
            });
            setSelectedLoan(res.data);
            setStep('detail');
            setErrors('');
        }catch(err){
            setErrors('Не удалось загрузить детали кредита');
            console.log(err);
        }finally{
            setIsLoading(false);
        }
    }

    const handlePayment = async(loanId) => {
        if (!window.confirm('Вы уверены, что хотите оплатить следующий платеж?')) return;
        try{
            await axios.post(`${API_URL}/loans/${loanId}/pay/`, {}, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('access')}`
                }
            });

            alert('Платеж успешно проведен');
            handleDetail(loanId);
            fetchLoans();
        }catch(err){
            setErrors('Ошибка при оплате кредита');
            console.log(err)
        }
    }

    if (isLoading && step != 'list') {return <div>Загрузка данных</div>}

    return(
        <div className="container">
            <h1>Управление кредитами</h1>
            {errors && <div className="alert alert-dander">{errors}</div>}
            {step === 'list' && (
                <div>
                    <button onClick={() => setStep('apply')}></button>
                    <h4>Мои кредиты</h4>
                    {loans.length === 0 ? (
                        <p>У вас нет активных кредитов</p>
                    ): (
                        <div className="row">
                            {loans.map((loan) => (
                                <div className="col-md-6 mb-3" key={loan.id}>
                                    <div className="card">
                                        <div className="card-body">
                                            <h5 className="card-title">Кредит №{loan.id}</h5>
                                            <p><strong>Сумма:</strong> {loan.amount} ₽</p>
                                            <p><strong>Статус:</strong> {loan.status}</p>
                                            <p><strong>Остаток:</strong> {loan.remaining_balance} ₽</p>
                                            <p><strong>Ежемесячно:</strong> {loan.monthly_payment} ₽</p>
                                            <button
                                                className="btn btn-info btn-sm me-2"
                                                onClick={() => handleDetail(loan.id)}
                                            >
                                                Детали
                                            </button>
                                            {/* Кнопка оплаты только для одобренных активных кредитов */}
                                            {loan.status === 'approved' && (
                                                <button
                                                    className="btn btn-success btn-sm"
                                                    onClick={() => handlePayment(loan.id)}
                                                >
                                                    Оплатить платёж
                                                </button>
                                            )}
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            )}
            {step === 'apply' && (
                <div className="card p-4 mb-4">
                    <h4>Подать заявку на кредит</h4>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <label>Счёт для зачисления</label>
                            <select
                                className="form-control"
                                value={formData.account_id}
                                onChange={(e) => setFormData({ ...formData, account_id: e.target.value })}
                                required
                            >
                                <option value="">Выберите счёт</option>
                                {accounts.map((acc) => (
                                    <option key={acc.id} value={acc.id}>
                                        {acc.account_type} (ID: {acc.id}, Баланс: {acc.balance} {acc.currency})
                                    </option>
                                ))}
                            </select>
                        </div>
                        <div className="mb-3">
                            <label>Сумма кредита (₽)</label>
                            <input
                                type="number"
                                className="form-control"
                                value={formData.amount}
                                onChange={(e) => setFormData({ ...formData, amount: e.target.value })}
                                min="1000"
                                step="100"
                                required
                            />
                        </div>
                        <div className="mb-3">
                            <label>Срок (месяцев)</label>
                            <input
                                type="number"
                                className="form-control"
                                value={formData.term_months}
                                onChange={(e) => setFormData({ ...formData, term_months: e.target.value })}
                                min="1"
                                max="60"
                                required
                            />
                        </div>
                        <button type="submit" className="btn btn-success">Подать заявку</button>
                        <button
                            type="button"
                            className="btn btn-secondary ms-2"
                            onClick={() => setStep('list')}
                        >
                            Отмена
                        </button>
                    </form>
                    </div>
            )}
            {step === 'detail' && selectedLoan && (
                <div>
                    <button className="btn btn-secondary mb-3" onClick={() => setStep('list')}>
                        ← Назад к списку
                    </button>
                    <div className="card p-4">
                        <h4>Кредит №{selectedLoan.loan.id}</h4>
                        <p><strong>Статус:</strong> {selectedLoan.loan.status}</p>
                        <p><strong>Сумма:</strong> {selectedLoan.loan.amount} ₽</p>
                        <p><strong>Процентная ставка:</strong> {selectedLoan.loan.interest_rate}%</p>
                        <p><strong>Ежемесячный платёж:</strong> {selectedLoan.loan.monthly_payment} ₽</p>
                        <p><strong>Остаток долга:</strong> {selectedLoan.loan.remaining_balance} ₽</p>
                        <p><strong>Дата начала:</strong> {new Date(selectedLoan.loan.start_date).toLocaleDateString()}</p>

                        <h5 className="mt-4">График платежей</h5>
                        <table className="table table-striped">
                            <thead>
                                <tr>
                                    <th>Дата платежа</th>
                                    <th>Сумма</th>
                                    <th>Статус</th>
                                </tr>
                            </thead>
                            <tbody>
                                {selectedLoan.payments.map((p) => (
                                    <tr key={p.id}>
                                        <td>{new Date(p.due_date).toLocaleDateString()}</td>
                                        <td>{p.amount} ₽</td>
                                        <td>
                                            {p.is_paid ? (
                                                <span className="badge bg-success">Оплачен</span>
                                            ) : (
                                                <span className="badge bg-warning text-dark">Не оплачен</span>
                                            )}
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>

                        {/* Кнопка оплаты видна только для одобренных кредитов */}
                        {selectedLoan.loan.status === 'approved' && (
                            <button
                                className="btn btn-success mt-3"
                                onClick={() => handlePayment(selectedLoan.loan.id)}
                            >
                                Оплатить следующий платёж
                            </button>
                        )}
                    </div>
                </div>
            )}
        </div>
    )
}

export default LoanManager;
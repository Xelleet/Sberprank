export const API_URL = 'http://127.0.0.1:8000/api';

const apiRequest = async (method, endpoint, data = null) => {
  const token = localStorage.getItem('access');
  console.log(token);
  const config = {
method,
headers: {
'Content-Type': 'application/json',
'Authorization': token ? `Bearer ${token}` : '',
},
body: data ? JSON.stringify(data) : null,
};
const response = await fetch(API_URL + endpoint, config);
if (!response.ok) {
const errorMsg = await response.text();
throw new Error(errorMsg);
}
return await response.json();
};


// --- конкретные API вызовы ---
export const loginUser = (credentials) =>
  apiRequest('POST', '/users/login/', credentials);

export const registerUser = (userData) =>
  apiRequest('POST', '/users/register/', userData);

export const fetchAccounts = () =>
  apiRequest('GET', '/accounts/');

export const transferMoney = (transferData) =>
  apiRequest('POST', '/transactions/transfer/', transferData);

export default apiRequest;

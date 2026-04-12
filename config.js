/* config.js — Central configuration. Update URLs to match your deployment. */

const BACKEND_URL  = "http://127.0.0.1:5000";
const FRONTEND_URL = "http://127.0.0.1:5001";

const CONFIG = {
  BACKEND_URL,
  ROUTES: {
    LOGIN:    `${FRONTEND_URL}/Login.html`,
    REGISTER: `${FRONTEND_URL}/Register.html`,
    FORGOT:   `${FRONTEND_URL}/Forgot.html`,
    CODE_OTP: `${FRONTEND_URL}/EmailCode.html`,
    MAIN:     `${FRONTEND_URL}/`,
    CODE:     `${FRONTEND_URL}/Code.html`,
  },
  API: {
    LOGIN:    `${BACKEND_URL}/Login`,
    REGISTER: `${BACKEND_URL}/Register`,
    FORGOT:   (email) => `${BACKEND_URL}/Forgot/${encodeURIComponent(email)}`,
    CODE:     (code, password) =>
      password
        ? `${BACKEND_URL}/Code/${encodeURIComponent(code)}/${encodeURIComponent(password)}`
        : `${BACKEND_URL}/Code/${encodeURIComponent(code)}`,
    MAIN:     `${BACKEND_URL}/`,
  },
};

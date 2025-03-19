"use client";

import styles from "./page.module.css";
import { useState } from "react";
import Link from "next/link";

export default function Signup() {
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [passwordVisible, setPasswordVisible] = useState(false);
  const [confirmPasswordVisible, setConfirmPasswordVisible] = useState(false);
  const [error, setError] = useState("");

  const togglePasswordVisibility = () => {
    setPasswordVisible((prev) => !prev);
  };

  const toggleConfirmPasswordVisibility = () => {
    setConfirmPasswordVisible((prev) => !prev);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      setError("Passwords do not match!");
      return;
    }

    setError(""); // Clear error if passwords match

    // Submit form data (you can add API call logic here)
    console.log("Form submitted successfully");
  };

  return (
    <>
      <div className={styles.login_page}>
        <div className={styles.login_container}>
          <div className={styles.content_wrapper}>
            <div className={styles.login_box}>
              <form className={styles.form} onSubmit={handleSubmit}>
                <h1 className={styles.h1}>Sign Up</h1>
                <p className={styles.paragraph}>
                  By Signing up you can access your previous predicted data.
                </p>

                <div className={styles.flex_column}>
                  <label className={styles.input_label}>Email</label>
                </div>
                <div className={styles.inputForm}>
                  <input
                    type="email"
                    className={styles.input}
                    placeholder="Enter your Email"
                    required
                  />
                </div>

                <div className={styles.flex_column}>
                  <label className={styles.input_label}>Password</label>
                </div>
                <div className={styles.inputForm}>
                  <input
                    type={passwordVisible ? "text" : "password"}
                    className={styles.input}
                    placeholder="Enter your Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    height="24px"
                    viewBox="0 -960 960 960"
                    width="24px"
                    fill="#000"
                    className={styles.eye_svg}
                    onClick={togglePasswordVisibility}
                  >
                    {passwordVisible ? (
                      <path d="M480-320q75 0 127.5-52.5T660-500q0-75-52.5-127.5T480-680q-75 0-127.5 52.5T300-500q0 75 52.5 127.5T480-320Zm0-72q-45 0-76.5-31.5T372-500q0-45 31.5-76.5T480-608q45 0 76.5 31.5T588-500q0 45-31.5 76.5T480-392Zm0 192q-146 0-266-81.5T40-500q54-137 174-218.5T480-800q146 0 266 81.5T920-500q-54 137-174 218.5T480-200Zm0-300Zm0 220q113 0 207.5-59.5T832-500q-50-101-144.5-160.5T480-720q-113 0-207.5 59.5T128-500q50 101 144.5 160.5T480-280Z" />
                    ) : (
                      <path d="m644-428-58-58q9-47-27-88t-93-32l-58-58q17-8 34.5-12t37.5-4q75 0 127.5 52.5T660-500q0 20-4 37.5T644-428Zm128 126-58-56q38-29 67.5-63.5T832-500q-50-101-143.5-160.5T480-720q-29 0-57 4t-55 12l-62-62q41-17 84-25.5t90-8.5q151 0 269 83.5T920-500q-23 59-60.5 109.5T772-302Zm20 246L624-222q-35 11-70.5 16.5T480-200q-151 0-269-83.5T40-500q21-53 53-98.5t73-81.5L56-792l56-56 736 736-56 56ZM222-624q-29 26-53 57t-41 67q50 101 143.5 160.5T480-280q20 0 39-2.5t39-5.5l-36-38q-11 3-21 4.5t-21 1.5q-75 0-127.5-52.5T300-500q0-11 1.5-21t4.5-21l-84-82Zm319 93Zm-151 75Z" />
                    )}
                  </svg>
                </div>

                <div className={styles.flex_column}>
                  <label className={styles.confirm_password}>
                    Confirm Password
                  </label>
                </div>
                <div className={styles.inputForm}>
                  <input
                    type={confirmPasswordVisible ? "text" : "password"}
                    className={styles.input}
                    placeholder="Confirm your Password"
                  />
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    height="24px"
                    viewBox="0 -960 960 960"
                    width="24px"
                    fill="#000"
                    className={styles.eye_svg}
                    onClick={toggleConfirmPasswordVisibility}
                  >
                    {confirmPasswordVisible ? (
                      <path d="M480-320q75 0 127.5-52.5T660-500q0-75-52.5-127.5T480-680q-75 0-127.5 52.5T300-500q0 75 52.5 127.5T480-320Zm0-72q-45 0-76.5-31.5T372-500q0-45 31.5-76.5T480-608q45 0 76.5 31.5T588-500q0 45-31.5 76.5T480-392Zm0 192q-146 0-266-81.5T40-500q54-137 174-218.5T480-800q146 0 266 81.5T920-500q-54 137-174 218.5T480-200Zm0-300Zm0 220q113 0 207.5-59.5T832-500q-50-101-144.5-160.5T480-720q-113 0-207.5 59.5T128-500q50 101 144.5 160.5T480-280Z" />
                    ) : (
                      <path d="m644-428-58-58q9-47-27-88t-93-32l-58-58q17-8 34.5-12t37.5-4q75 0 127.5 52.5T660-500q0 20-4 37.5T644-428Zm128 126-58-56q38-29 67.5-63.5T832-500q-50-101-143.5-160.5T480-720q-29 0-57 4t-55 12l-62-62q41-17 84-25.5t90-8.5q151 0 269 83.5T920-500q-23 59-60.5 109.5T772-302Zm20 246L624-222q-35 11-70.5 16.5T480-200q-151 0-269-83.5T40-500q21-53 53-98.5t73-81.5L56-792l56-56 736 736-56 56ZM222-624q-29 26-53 57t-41 67q50 101 143.5 160.5T480-280q20 0 39-2.5t39-5.5l-36-38q-11 3-21 4.5t-21 1.5q-75 0-127.5-52.5T300-500q0-11 1.5-21t4.5-21l-84-82Zm319 93Zm-151 75Z" />
                    )}
                  </svg>
                </div>

                {error && <p className={styles.error}>{error}</p>}

                <button type="submit" className={styles.button_submit}>
                  Sign Up
                </button>

                <p className={styles.p}>
                  Already have an account?{" "}
                  <Link href="/login">
                    <span className={styles.span}>Login</span>
                  </Link>
                </p>
              </form>
            </div>

            {/* New Div */}
            <div className={styles.additional_info}>
              <h2>Predict Better. Perform Better</h2>
              <p>
                Your teams's potential is limitless-- <br />
                all it needs is the right insight.
              </p>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

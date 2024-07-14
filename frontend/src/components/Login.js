import React from 'react'
import styles from '../styles/register.module.css'


const Login = () => {
  return (
    <>
      <div className="container mt-5">
        <div className={styles.formContainer}>
          <form action="">
            <div className="row">
              <div className="col-12">
                <div className={styles.title}>
                  <h1>Login</h1>
                </div>
                <div className={styles.forms}>
                  <div className={styles.input_field2}>
                    <span>Email</span>
                    <input type="email" className='input' name='email' placeholder='' />
                  </div>
                  <div className={styles.input_field2}>
                    <span>Password</span>
                    <input type="password" className='input' name='password' placeholder='' />
                  </div>
                  <div className={styles.button1}>
                    <button type="button" class="btn btn-primary">Login</button>
                  </div>
                  <div className={styles.google}>
                    <p>Singup using Google</p>
                    <p>Signup using email address</p>
                  </div>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </>
  )
}

export default Login

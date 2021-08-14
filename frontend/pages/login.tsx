import styles from '../styles/login.module.css';

const Login = () => {
    return(
        <div className={styles.background}>
            <div className={styles.login_form}>
                <div className={styles.greeting}>
                    <h1 className={styles.title}>Welcome back to <span>Portfolio Creator</span></h1>
                    <p className={styles.description}>Login to access your saved websites!</p>
                </div>
                <div className={styles.login_inputs}>
                    <input type="text" placeholder="Email"/>
                    <br />
                    <input type="text" placeholder="Password"/>
                </div>
                <button className={styles.login}>Login</button>
            </div>
        </div>
    )
}

export default Login;
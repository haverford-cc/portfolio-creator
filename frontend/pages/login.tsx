import styles from '../styles/login.module.css';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import Navbar from '../components/Navbar/Narbar';

const Login = () => {

    const initialValues = {
        email: '',
        password: ''
    }

    const formSchema = Yup.object().shape({
        email: Yup.string().required('Required'),
        password: Yup.string().required('Required')
    })

    const formSubmission = (values) => {

    }

    return(
        <div className={styles.background}>
            <Navbar />
            <Formik initialValues={initialValues} onSubmit={formSubmission} validationSchema={formSchema} className={styles.login_form}>
                <Form className={styles.login_form}>
                    <div className={styles.greeting}>
                        <h1 className={styles.title}>Welcome back to <span>Portfolio Creator</span></h1>
                        <p className={styles.description}>Login to access your saved websites!</p>
                    </div>
                    <div className={styles.login_inputs}>
                        <label>Username</label>
                        <ErrorMessage name="email" component="span"/>
                        <Field className={styles.input} type="text" name="email" placeholder="Email" />
                        <label>Password</label>
                        <ErrorMessage name="password" component="span"/>
                        <Field className={styles.input} type="password" name="password" placeholder="Password" />
                    </div>
                    <button className={styles.login}>Login</button>
                </Form>
            </Formik>
        </div>
    )
}

export default Login;
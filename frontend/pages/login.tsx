import styles from '../styles/login.module.css';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import Navbar from '../components/Navbar/Narbar';
import axios from 'axios';
import { useRouter } from 'next/router';

const Login = () => {

    const router = useRouter();

    const initialValues = {
        email: '',
        password: ''
    }   

    const formSchema = Yup.object().shape({
        email: Yup.string().email().required(' Required'),
        password: Yup.string().min(8).required(' Required')
    })

    type response = {
        email: string,
        password: string
    }

    const formSubmission = (values:response) => {
        // ApiClient.post('/auth/login', {
        //     email: values.email,
        //     password: values.password

        // }).then(response => {
        //     if(response.data.success) {
        //         router.push('/');
        //     }
        // })
    }

    return(
            <div className={styles.background}>
                <Navbar />
                <Formik initialValues={initialValues} onSubmit={formSubmission} validationSchema={formSchema}>
                    <Form className={styles["login-form"]}>
                        <h1 className={styles.title}>Welcome back to <span>Portfolio Creator</span></h1>
                        <p>Login to access your saved websites!</p>
                        <div>
                            <label>Email </label>
                            <ErrorMessage name="email">{msg => <span><span>&#8212;</span><span className={styles.span}>{` ${msg}`}</span></span>}</ErrorMessage>
                            <Field className={styles.input} type="text" name="email" placeholder="Email" />
                            <label>Password </label>
                            <ErrorMessage name="password">{msg => <span><span>&#8212;</span><span className={styles.span}>{` ${msg}`}</span></span>}</ErrorMessage>
                            <Field className={styles.input} type="password" name="password" placeholder="Password" />
                            <h3 className={styles["error-handlling"]}></h3>
                        </div>
                        <button className={styles.login} type="submit">Login</button>
                    </Form>

                </Formik>
            </div>
    )
}

export default Login;
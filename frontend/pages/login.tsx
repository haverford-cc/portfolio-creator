import { GetServerSideProps } from "next";
import { useRouter } from "next/router";

import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

import Navbar from "../components/Navbar/Narbar";
import { useApiClient } from "../hooks/api";
import styles from "../styles/Login.module.css";

type LoginProps = {
  host: string;
};

type LoginFormValues = {
  email: string;
  password: string;
};

const Login = (props: LoginProps) => {
  const router = useRouter();

  const { apiClient, setHost } = useApiClient();
  setHost(props.host);

  const initialValues = {
    email: "",
    password: "",
  };

  const formSchema = Yup.object().shape({
    email: Yup.string().email().required("Required"),
    password: Yup.string().min(8).required("Required"),
  });

  const formSubmission = (values: LoginFormValues) => {
    apiClient
      .post("/auth/login", {
       email: values.email,
        password: values.password,
      })
      .then(response => {
        if(response.data.success) router.push("/");
      })
      .catch(error => console.log(error.response.data.detail))
  };

  return (
    <div className={styles.background}>
      <Navbar />
      <Formik
        initialValues={initialValues}
        onSubmit={formSubmission}
        validationSchema={formSchema}
      >
        <Form className={styles["login-form"]}>
          <h1 className={styles.title}>Welcome back to Portfolio Creator</h1>
          <p>Login to access your saved websites!</p>
          <div>
            <label>Email</label>
            <ErrorMessage name="email">
              {(msg) => (
                <>
                  {" — "}
                  <span className={styles.span}>{msg}</span>
                </>
              )}
            </ErrorMessage>
            <Field
              className={styles.input}
              type="email"
              name="email"
              placeholder="Email"
            />
            <label>Password</label>
            <ErrorMessage name="password">
              {(msg) => (
                <>
                  {" — "}
                  <span className={styles.span}>{msg}</span>
                </>
              )}
            </ErrorMessage>
            <Field
              className={styles.input}
              type="password"
              name="password"
              placeholder="Password"
            />
          </div>
          <h3 className={styles["error-handling"]}></h3>
          <button className={styles.login}>Login</button>
        </Form>
      </Formik>
    </div>
  );
};

export const getServerSideProps: GetServerSideProps = async (context) => {
  return { props: { host: context.req.headers.host! } };
};

export default Login;

import React, {useContext, useEffect, useState} from 'react';
import InputField from "../../components/UI/InputField/InputField";
import Button from "../../components/UI/Button/Button";
import {UserContext} from "../../context/userContext";
import {useNavigate} from "react-router-dom";
import {loginAPI} from "../../API/Login";

const Login = () => {
    const [user, setUser] = useState({
        username: "",
        password: ""
    })
    const {userToken, setUserToken} = useContext(UserContext)

    const navigate = useNavigate();
    useEffect(() => {
        if (userToken !== null) {
            navigate("/", {replace: true});
        }
    }, [userToken, navigate])

    async function login(e) {
        e.preventDefault()
        const token = await loginAPI(
            user.username,
            user.password,
        )
        if (token) {
            setUserToken(token)
        }

    }

    return (
        <div>
            <h1 className="title is-3 is-flex is-justify-content-center mb-0 mt-4">
                Страница входа </h1>
            <form onSubmit={login}
                  className="box block is-flex is-flex-direction-column"
            >
                <InputField
                    label="E-mail"
                    placeholder="Электронная почта"
                    onChange={(e) => setUser({...user, username: e.target.value})}
                    value={user.username}
                />
                <InputField
                    isPassword
                    label="Пароль"
                    placeholder="Пароль"
                    onChange={(e) => setUser({...user, password: e.target.value})}
                    value={user.password}
                />

                <Button type="submit">Войти</Button>
            </form>

        </div>
    );
};

export default Login;
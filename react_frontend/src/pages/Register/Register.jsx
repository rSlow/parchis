import React, {useContext, useEffect, useState} from 'react';
import InputField from "../../components/UI/InputField/InputField";
import Button from "../../components/UI/Button/Button";
import {checkEmailAPI, checkUsernameAPI, registerUserAPI} from "../../API/Register"
import {UserContext} from "../../context/userContext";

const Register = () => {
    const {setUserToken} = useContext(UserContext)

    const [user, setUser] = useState({
        username: "",
        email: "",
        password: "",
        confirm_password: ""
    })

    const [isPasswordsNoEqual, setIsPasswordsNoEqual] = useState(false)
    const [isEmailExist, setIsEmailExist] = useState(false)
    const [isUsernameExist, setIsUsernameExist] = useState(false)

    useEffect(() => {
        setIsPasswordsNoEqual(user.password !== user.confirm_password)
    }, [user.password, user.confirm_password])

    useEffect(() => {
        if (user.email) {
            (async function checkEmail() {
                setIsEmailExist(await checkEmailAPI(user.email))
            })()
        }
    }, [user.email])

    useEffect(() => {
        if (user.username) {
            (async function () {
                setIsUsernameExist(await checkUsernameAPI(user.username))
            })()
        }
    }, [user.username])

    async function registerUser(event) {
        event.preventDefault()
        if (user.username && user.email && user.password && isPasswordsNoEqual !== true) {
            try {
                const response = await registerUserAPI(
                    user.email,
                    user.password,
                    user.username
                )
                setUserToken(response.data["access_token"])
            } catch (e) {
                console.log(e.response.data["detail"])
            }
        }
    }

    return (
        <div>
            <h1 className="title is-3 is-flex is-justify-content-center mb-0 mt-4"> Страница регистрации </h1>
            <form onSubmit={registerUser}
                  className="box block is-flex is-flex-direction-column"
            >
                <InputField
                    label="Логин"
                    placeholder="Логин"
                    onChange={(e) => setUser({...user, username: e.target.value})}
                    value={user.username}
                    errorFlag={isUsernameExist}
                    errorMessage={"Аккаунт с таким именем уже существует."}
                />
                <InputField
                    label="E-mail"
                    placeholder="Электронная почта"
                    type="email"
                    onChange={(e) => setUser({...user, email: e.target.value})}
                    value={user.email}
                    errorFlag={isEmailExist}
                    errorMessage={"Аккаунт с такой электронной почтой уже существует."}
                />
                <InputField
                    isPassword
                    label="Пароль"
                    placeholder="Пароль"
                    onChange={(e) => setUser({...user, password: e.target.value})}
                    value={user.password}
                />
                <InputField
                    isPassword
                    label="Подтвердите пароль"
                    placeholder="Подтверждение пароля"
                    onChange={(e) => setUser({...user, confirm_password: e.target.value})}
                    value={user.confirm_password}
                    errorFlag={isPasswordsNoEqual}
                    errorMessage="Пароли не совпадают!"
                />

                <Button type="submit">Зарегистрироваться</Button>
            </form>
        </div>
    );
};

export default Register;
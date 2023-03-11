import React, {useState} from 'react';
import classes from "./Header.module.css";

const Header = () => {
    const [isAuth, setIsAuth] = useState(false)

    return (
        <div className={classes.header}>
            <div className={classes.app_name}>
                Мандавошка
            </div>
            {isAuth
                ? <div className={classes.user_block}>
                    Профиль
                </div>
                : <div className={classes.user_block}>
                    <div className={classes.user_block__button}>
                        Войти
                    </div>
                    |
                    <div className={classes.user_block__button}>
                        Регистрация
                    </div>
                </div>
            }
        </div>
    );
};

export default Header;
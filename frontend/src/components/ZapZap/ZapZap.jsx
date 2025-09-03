import React, { useState } from "react";
import styles from './ZapZap.module.css';
import zapLogo from "../../assets/zapzap.svg";

function ZapZap() {

    const [response, setResponse] = useState("");
    const [target, setTarget] = useState("");

    const [selectedTags, setSelectedTags] = useState([]);
    const availableTags = [
        "fofo", "apaixonado", "saudade",
        "reconfortar", "bom-dia", "boa-noite",
        "aleatorio", "emoji"
    ];

    const handleResponse = () => {
        const query = selectedTags.length ? `?tags=${selectedTags.join(",")}` : "";
        fetch('http://127.0.0.1:5000/generate' + query)
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro na req');
            }
            return response.json();
        })
        .then(data => {
            setResponse(data.response);
        })
        .catch(error => {
            console.log("Erro: ", error)
        });
    }

    const handleSendToTarget = () => {
        let inputTarget = document.getElementById('target').value;

        let onlyNumbers = inputTarget.replace(/\D/g, "");

        if (!onlyNumbers.startsWith("55")) {
            onlyNumbers = "55" + onlyNumbers;
        }

        let formatted = "+" + onlyNumbers;

        if (!/^\+55\d{10,11}$/.test(formatted)) {
            alert("Por favor, insira um número de telefone válido.");
            return;
        }

        setTarget(formatted);

        if (response === "") {
            alert("Por favor, gere uma mensagem fofa.");
            return;
        }

        handleWhatsAppRedirect(formatted);
    };


    function handleWhatsAppRedirect(inputTarget) {
        
        const url = 'http://127.0.0.1:5000/send';
        
        const dataToSend = {
            numberTarget: {inputTarget},
            aiResponse: {response}
        };

        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dataToSend)
        };

        fetch(url, options)
        .then(response => {
            if (!response.ok) {
            throw new Error(`Erro HTTP! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Sucesso:', data);
        })
        .catch(error => {
            console.error('Erro na requisição:', error);
        });
    }

    const getResponse = () => {
        return (
            <div>
                {response}
            </div>
        )
    }

    return (
        <div className={styles["main-container"]}>
            
            <div className={styles["head"]}>
                <h1>ZapZap <span id={styles["love-markup"]}>Love</span>Bot</h1>
                <img src={zapLogo} alt="" />
            </div>
            
            <div className={styles["container"]}>

                <p>Developed by Tuchanski</p>

                <div className={styles["user-input"]}>
                    <label htmlFor="">Número do WhatsApp</label>
                    <input id="target" type="text" placeholder="+55 (41) 99999-9999"/>

                    <div className={styles["tags-container"]}>
                        
                        {availableTags.map((tag) => {
                            const isSelected = selectedTags.includes(tag);
                            return (
                            <span
                                key={tag}
                                className={`${styles["tag"]} ${isSelected ? styles["tag-selected"] : ""}`}
                                onClick={() => {
                                if (isSelected) {
                                    setSelectedTags(selectedTags.filter((t) => t !== tag));
                                } else {
                                    setSelectedTags([...selectedTags, tag]);
                                }
                                }}
                            >
                                {tag}
                            </span>
                            );
                        })}
                    </div>

                    <button className={styles["btn-system"]} onClick={handleResponse}>Gerar Mensagem...</button>
                </div>

                <div className={styles["response"]}>
                    <h2>Mensagem Gerada</h2>
                    {getResponse()}
                    <button className={styles["btn-system"]} onClick={handleSendToTarget}>Enviar via WhatsApp</button>
                </div>

                <p id={styles["footer"]}>Powered by <span id={styles["llama-ref"]}>llama 3.3</span></p>

            </div>
        </div>   
    )

}

export default ZapZap;
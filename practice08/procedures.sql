-- Добавление или обновление
CREATE OR REPLACE PROCEDURE upsert_user(p_name VARCHAR, p_surname VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM contacts 
        WHERE name = p_name AND surname = p_surname
    ) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name AND surname = p_surname;
    ELSE
        INSERT INTO contacts(name, surname, phone)
        VALUES (p_name, p_surname, p_phone);
    END IF;
END;
$$;


-- Массовая вставка с проверкой
CREATE OR REPLACE PROCEDURE insert_many_users(
    names TEXT[],
    surnames TEXT[],
    phones TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    invalid_data TEXT[] := ARRAY[]::TEXT[];
BEGIN
    FOR i IN 1..array_length(names, 1)
    LOOP
        IF phones[i] ~ '^\+?[0-9]+$' THEN
            CALL upsert_user(names[i], surnames[i], phones[i]);
        ELSE
            invalid_data := array_append(invalid_data, phones[i]);
        END IF;
    END LOOP;

    RAISE NOTICE 'Invalid phones: %', invalid_data;
END;
$$;


-- Удаление
CREATE OR REPLACE PROCEDURE delete_user(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value
       OR phone = p_value;
END;
$$;
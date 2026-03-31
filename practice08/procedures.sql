CREATE OR REPLACE PROCEDURE add_new_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO contacts (name, phone) VALUES (p_name, p_phone);
END;
$$;
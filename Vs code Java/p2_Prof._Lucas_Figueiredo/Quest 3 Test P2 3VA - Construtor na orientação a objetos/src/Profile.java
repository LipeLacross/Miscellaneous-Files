public class Profile {
    private String name;
    private String id;

    public Profile() {
        // Construtor sem parâmetros
        this.name = "";
        this.id = "";
    }

    public Profile(String name, String id) {
        // Construtor que recebe os parâmetros necessários
        this.name = name;
        this.id = id;
    }

    // Getters e Setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
}

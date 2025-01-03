<script lang=ts>
    import { databases } from '$lib/api';

    let documents = [];

    async function fetchDocuments() {
        try {
            const response = await databases.listDocuments('myDatabase', 'users');
            documents = response.documents;
        } catch (error) {
            console.error('Error fetching documents:', error);
        }
    }

    fetchDocuments();
</script>

<h1>Some Users</h1>
<ul>
    {#each documents as doc}
        <li>{doc.name} ({doc.email})</li>
    {/each}
</ul>


<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>

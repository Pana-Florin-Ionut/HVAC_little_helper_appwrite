<script lang=ts>
    import { databases } from '$lib/api';

    let documents = [];

    async function fetchDocuments() {
        try {
            const response = await databases.listDocuments('6776d72d0012b3501f45', '6776d73e002b2db59445');
            documents = response.documents;
            console.log("Documents: " + JSON.stringify(documents, null, 2))
        } catch (error) {
            console.error('Error fetching documents:', error);
        }
    }

    fetchDocuments();
</script>

<h1>Some Users</h1>
<ul>
    {#each documents as doc}
        <li>{doc.Name} ({doc.Age})</li>
    {/each}
</ul>


<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>

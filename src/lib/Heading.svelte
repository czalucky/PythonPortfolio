<script>
    let menuButton;
</script>

<div>
    <h1 class="flex flex-row justify-between p-4 bg-green-800 text-white">
        <div class="left-0 top-6 text-sm">SEI Investments</div>
        <div class="text-4xl text-center font-bold"><slot /></div>

        <div>        
            <button class="h-16 w-16 md:space-y-0 fixed bottom-4 md:top-1 right-4 rounded-full cursor-pointer pointer-events-auto p-4" bind:this={menuButton} id="menubutton" aria-haspopup="true" aria-controls="main-menu">
                <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-menu-2 pointer-events-none" viewBox="0 0 24 24" stroke-width="1.7" stroke="#FFFFFF" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                    <line x1="4" y1="6" x2="20" y2="6" />
                    <line x1="4" y1="12" x2="20" y2="12" />
                    <line x1="4" y1="18" x2="20" y2="18" />
                </svg>
            </button>
        </div>
    </h1>
</div>
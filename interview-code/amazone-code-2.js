function RemoveOccurrences(arr, remove) {
    const index = arr.indexOf(remove);
    if (index > -1) {
        arr.splice(index, 1);
    }
}
